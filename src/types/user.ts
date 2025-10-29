/**
 * User type definitions
 * [Source: docs/architecture.md#data-models]
 */

export interface User {
  id: string;
  email: string;
  password: string;
  emailVerified: boolean;
  createdAt: Date;
  updatedAt: Date;
}

/**
 * User response type - excludes password field
 * Used in API responses to ensure password is never exposed
 */
export type UserResponse = Omit<User, 'password'>;

export interface SignupResponse {
  user: UserResponse;
  token: string;
}
