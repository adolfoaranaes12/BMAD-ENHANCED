import bcrypt from 'bcrypt';
import { UserRepository } from '../../repositories/user.repository';
import { UserResponse } from '../../types/user';

/**
 * Signup service - implements user registration business logic
 * [Source: docs/architecture.md#api-specifications]
 */
export class SignupService {
  private userRepository: UserRepository;
  private readonly BCRYPT_COST = 12; // [Source: docs/standards.md#password-security]

  constructor(userRepository: UserRepository) {
    this.userRepository = userRepository;
  }

  /**
   * Register a new user with email and password
   * @throws Error if email already exists (409)
   * @throws Error if database operation fails (500)
   */
  async signup(email: string, password: string): Promise<UserResponse> {
    // Check for duplicate email [AC: 4]
    const existingUser = await this.userRepository.findByEmail(email);
    if (existingUser) {
      const error = new Error('Email already registered');
      (error as any).statusCode = 409;
      throw error;
    }

    // Hash password with bcrypt [AC: 5]
    // [Source: docs/standards.md#password-security]
    const hashedPassword = await bcrypt.hash(password, this.BCRYPT_COST);

    // Create user in database [AC: 1]
    try {
      const user = await this.userRepository.createUser(email, hashedPassword);

      // Return user without password field [AC: 6]
      const { password: _, ...userResponse } = user;
      return userResponse;
    } catch (error) {
      // Handle database errors [AC: error handling]
      const dbError = new Error('An unexpected error occurred');
      (dbError as any).statusCode = 500;
      throw dbError;
    }
  }
}
